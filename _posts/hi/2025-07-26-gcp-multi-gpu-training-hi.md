---
audio: false
generated: true
lang: hi
layout: post
title: एनवीआईडीआईए जीपीयू के साथ जीसीपी पर एमएल मॉडल प्रशिक्षण
translated: true
type: note
---

Google Cloud Platform (GCP) NVIDIA GPUs का उपयोग करके मशीन लर्निंग मॉडल को ट्रेन करने के लिए Vertex AI (मैनेज्ड ट्रेनिंग जॉब्स के लिए) और Compute Engine (कस्टम वर्चुअल मशीनों के लिए) जैसी सेवाओं के माध्यम से मजबूत विकल्प प्रदान करता है। हालाँकि, NVIDIA RTX 4090 GPUs GCP पर उपलब्ध नहीं हैं। RTX 4090 एक कंज्यूमर-ग्रेड GPU है जो मुख्य रूप से डेस्कटॉप और गेमिंग के लिए है, न कि क्लाउड डेटा सेंटर के लिए डिज़ाइन किया गया है। इसके बजाय, GCP एंटरप्राइज-ग्रेड NVIDIA GPUs प्रदान करता है जैसे कि A100, H100, L4, और अन्य, जो AI वर्कलोड के लिए ऑप्टिमाइज़्ड हैं और अक्सर उच्च मेमोरी बैंडविड्थ और टेंसर कोर दक्षता के कारण ट्रेनिंग परिदृश्यों में RTX 4090 से बेहतर प्रदर्शन करते हैं।

मल्टी-GPU सेटअप (कम से कम 2 GPUs) के लिए, आप मशीन प्रकार के आधार पर 2, 4, 8, या अधिक GPUs का उपयोग करने के लिए संसाधनों को कॉन्फ़िगर कर सकते हैं। मैं सादगी के लिए Vertex AI पर ध्यान केंद्रित करूंगा, क्योंकि यह ML ट्रेनिंग के लिए तैयार किया गया है और स्केलिंग को स्वचालित रूप से संभालता है। यदि आपको अधिक नियंत्रण की आवश्यकता है, तो मैं Compute Engine को संक्षेप में कवर करूंगा।

## पूर्वापेक्षाएँ
- एक Google Cloud खाता सेट अप करें और एक प्रोजेक्ट बनाएँ।
- अपने प्रोजेक्ट में Vertex AI API और Compute Engine API सक्षम करें।
- Google Cloud SDK (gcloud CLI) और Vertex AI SDK इंस्टॉल करें (यदि Python का उपयोग कर रहे हैं)।
- अपने ट्रेनिंग कोड को एक Docker कंटेनर में तैयार करें (उदाहरण के लिए, TensorFlow या PyTorch का उपयोग करके जिसमें Horovod या torch.distributed जैसी डिस्ट्रिब्यूटेड ट्रेनिंग सपोर्ट शामिल हो)।
- सुनिश्चित करें कि आपका मॉडल कोड मल्टी-GPU ट्रेनिंग को सपोर्ट करता है (उदाहरण के लिए, PyTorch में DataParallel या DistributedDataParallel के माध्यम से)।

## मल्टी-GPU ट्रेनिंग के लिए Vertex AI का उपयोग करना
Vertex AI, ML वर्कफ़्लो के लिए GCP का मैनेज्ड प्लेटफ़ॉर्म है। यह कस्टम ट्रेनिंग जॉब्स का समर्थन करता है जहां आप कई GPUs वाले मशीन प्रकार निर्दिष्ट कर सकते हैं।

### मल्टी-GPU के लिए उपलब्ध GPU प्रकार
सामान्य NVIDIA GPUs जो कम से कम 2 अटैचमेंट को सपोर्ट करते हैं:
- NVIDIA H100 (80GB या Mega 80GB): बड़े मॉडलों के लिए उच्च-प्रदर्शन; 2, 4, या 8 GPUs को सपोर्ट करता है।
- NVIDIA A100 (40GB या 80GB): ट्रेनिंग के लिए व्यापक रूप से उपयोग किया जाता है; 2, 4, 8, या 16 GPUs को सपोर्ट करता है।
- NVIDIA L4: इन्फ़रेंस और हल्की ट्रेनिंग के लिए लागत-प्रभावी; 2, 4, या 8 GPUs को सपोर्ट करता है।
- NVIDIA T4 या V100: पुराने लेकिन अभी भी उपलब्ध; 2, 4, या 8 GPUs को सपोर्ट करता है।

पूरी सूची में GB200, B200, H200, P4, P100 शामिल हैं - उपलब्धता के लिए क्षेत्रों की जाँच करें, क्योंकि सभी हर ज़ोन में उपलब्ध नहीं हैं।

### कम से कम 2 GPUs के साथ एक ट्रेनिंग जॉब बनाने के चरण
1. **अपना कंटेनर तैयार करें**: अपनी ट्रेनिंग स्क्रिप्ट के साथ एक Docker इमेज बनाएं और उसे Google Container Registry या Artifact Registry पर पुश करें। PyTorch के लिए उदाहरण Dockerfile:
   ```
   FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
   COPY train.py /app/train.py
   WORKDIR /app
   CMD ["python", "train.py"]
   ```

2. **gcloud CLI का उपयोग करके जॉब को कॉन्फ़िगर करें**:
   - एक `config.yaml` फ़ाइल बनाएँ:
     ```yaml
     workerPoolSpecs:
       machineSpec:
         machineType: a3-highgpu-2g  # उदाहरण: 2x H100 GPUs; विकल्प: a2-ultragpu-2g (2x A100), g2-standard-24 (2x L4)
         acceleratorType: NVIDIA_H100_80GB  # या NVIDIA_A100_80GB, NVIDIA_L4
         acceleratorCount: 2  # कम से कम 2
       replicaCount: 1
       containerSpec:
         imageUri: gcr.io/your-project/your-image:latest  # आपकी Docker इमेज URI
     ```
   - कमांड चलाएँ:
     ```bash
     gcloud ai custom-jobs create \
       --region=us-central1 \  # GPU उपलब्धता वाला एक क्षेत्र चुनें
       --display-name=your-training-job \
       --config=config.yaml
     ```

3. **Python SDK का उपयोग करना**:
   ```python
   from google.cloud import aiplatform

   aiplatform.init(project='your-project-id', location='us-central1')

   job = aiplatform.CustomJob(
       display_name='your-training-job',
       worker_pool_specs=[
           {
               'machine_spec': {
                   'machine_type': 'a3-highgpu-2g',  # 2x H100
                   'accelerator_type': 'NVIDIA_H100_80GB',
                   'accelerator_count': 2,
               },
               'replica_count': 1,
               'container_spec': {
                   'image_uri': 'gcr.io/your-project/your-image:latest',
               },
           }
       ],
   )
   job.run()
   ```

4. **मॉनिटर और स्केल करें**:
   - जॉब स्टेटस और लॉग देखने के लिए Vertex AI कंसोल का उपयोग करें।
   - कई मशीनों में डिस्ट्रिब्यूटेड ट्रेनिंग के लिए (उदाहरण के लिए, अधिक रेप्लिका), अतिरिक्त वर्कर पूल जोड़ें और बड़े पैमाने की जॉब्स के लिए यदि आवश्यक हो तो रिडक्शन सर्वर का उपयोग करें।
   - लागत: GPUs का बिल प्रति घंटे के आधार पर लगता है; अपने क्षेत्र में मूल्य निर्धारण की जाँच करें (उदाहरण के लिए, 2x H100 की लागत ~$6-10/घंटा हो सकती है)।

5. **मल्टी-GPU ट्रेनिंग के लिए सुझाव**:
   - अपने कोड में डिस्ट्रिब्यूटेड ट्रेनिंग सक्षम करें (उदाहरण के लिए, `torch.nn.parallel.DistributedDataParallel`)।
   - यदि रुकावटें स्वीकार्य हैं तो लागत बचत के लिए स्पॉट VMs या रिज़र्वेशन का उपयोग करें।
   - GCP कंसोल के माध्यम से अपने क्षेत्र/ज़ोन में GPU उपलब्धता सत्यापित करें।

## विकल्प: Compute Engine VMs का उपयोग करना
यदि आप Vertex AI के बिना कस्टम सेटअप पसंद करते हैं:
1. एक VM इंस्टेंस बनाएँ:
   - Compute Engine > VM instances > Create instance पर जाएँ।
   - मशीन प्रकार: A3 (H100), A2 (A100), G2 (L4) श्रृंखला से चुनें, उदाहरण के लिए, 2x H100 के लिए `a3-highgpu-2g`।
   - बूट डिस्क: एक Deep Learning VM इमेज का उपयोग करें (CUDA, TensorFlow/PyTorch प्री-इंस्टॉल्ड के साथ)।
   - GPUs जोड़ें: चुने गए प्रकार के 2 एक्सेलेरेटर निर्दिष्ट करें।

2. VM में SSH करें और अपनी ट्रेनिंग स्क्रिप्ट चलाएँ:
   ```bash
   gcloud compute ssh your-vm-name --zone=your-zone
   python train.py  # सुनिश्चित करें कि CUDA डिटेक्ट हो रहा है: nvidia-smi
   ```

3. मल्टी-GPU के लिए: आपके कोड को इसे हैंडल करना होगा (उदाहरण के लिए, `CUDA_VISIBLE_DEVICES=0,1`)।

यह अधिक हाथों से काम करने वाला है लेकिन पूर्ण नियंत्रण देता है।

## सीमाएँ और विकल्प
- यदि आपको विशेष रूप से RTX 4090 जैसा प्रदर्शन चाहिए, तो AWS (जो कुछ मामलों में कंज्यूमर GPUs प्रदान करता है) या ऑन-प्रिमाइसेस सेटअप जैसे विकल्पों पर विचार करें।
- मुफ्त/सीमित GPU ट्रेनिंग के लिए, Google Colab आज़माएँ (1-2 GPUs तक, लेकिन मल्टी-GPU या 4090-समकक्ष की गारंटी नहीं है)।
- कोटा की हमेशा जाँच करें और यदि आवश्यक हो तो GCP कंसोल के माध्यम से वृद्धि का अनुरोध करें।

[Configure compute resources for custom training | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/training/configure-compute)  
[GPU machine types | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/gpus)  
[Cloud GPUs (Graphics Processing Units) - Google Cloud](https://cloud.google.com/gpu)