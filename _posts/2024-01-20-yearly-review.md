---
layout: post
title: "Year in Review: 2023"
---

How to summarize my experience in 2023? Is it succesful or not? How to measure it? How I feel about it? It is a long story.

Around November 2022, I got two offers from two companies whose client is a big bank. They compete for me. One is give me around 27k CNY salary a month, another is 32k CNY salary a month. I choosed to join the second one. The previous job I took gave me the monthly salary around 22k. So I got the salary increase about 50%. I felt pretty good at the start of this year.

Though I already got the salary of 25k a month in 2017, it has no much increase comparing that. I know, another 5 years passed, I growed. And comparing previous Chinese statup job and my startup company business, now my daily hour rate was higher than ever. My brain was sharper than ever.

And because of 3 years of COVID period, I seldom to go to travel. So when coming back from Xining, my hometown, I began to travel for some places using my DJI Drone to shoot some scenarios. I went to the tower of Guangzhou and then I made a short video.

The interesting thing about that short video is that the background music rhyme of the video is matched to the lights alongside the river in some point. At that time, the rhyme changes, the lights change from on to off. 

And then about a month, every weekend I went outside, mainly around Greater Bay Area in China. Zhuhai, Dongguan, Macau, Beihai, Zhaoqing, Qingyuan. And I practice to use DJI Drone to take arieal views. 

The most nervous moments is that when I was in Macao, when I took the scenario in a place nearby a lake. I remoted control the DJI Drone to fly above the lake. However, the drone began to drop down. I remoted control it to fly from the above the land to the lake. Suddenly, the distance between it and the below surface was changed. It may be lead to some problems and make it begin to drop. I was nervous and quickly want to grasp it with my hand as it is still nearby the

The new job I do is about a payment app. I helped do some backend development using Java, Spring, Spring Cloud, Azure and do some AWS migration.

I learned a lot in this journey. Let me describe about some technical lessons.

* Software architecture is very important. The microservice structure is often better than monolithic application for large backend application. It is better to develop and deploy the code. We should think about how we structure the code in the long term view. 

* Azure EventHub Kafka propeties config is important. If we do it wrong, we may lose messages when the microservices scale up.

* Sometimes, We can check the build.log of the IDEA to fix bug.

* Every line of the code matters. We can directly jump to the location of the new code to check and suspect. Like why the log here isn't printed out.

* We should do the right thing as early as possible. If something is wrong, the problem is always there and keeps making trouble to us.

* It is hard to do the right thing. We should try it for a lot of ways and let the reality tell us what is best. We can only learn some precious lessons when we stay long enough. So it is important to keep notes about our decisions and reflect on them after some time. For the code too, it is same too.

* We should write down our technical notes and precious lessons correctly in time. After some time, you may forget what is exactly happen.

* SSH Tunneling for 3 times is hard to understand sometimes. Use verbose mode to check carefully.

* Life is connecting dots. Debuging or coding is about connecting messages. To fix the bug of the backend code, we can check the frontend code too. My commitment in Anroid and iOS development between 2014 to 2016 was not a matter of wasting time though now I worked mainly as backend developer. 

And during this time, ChatGPT is hot. I began to read the book "Neural Networks and Deep Learning". Around the June, I read probably half of it. I felt I begin to understand them. Then I tried to implement the neural network from scratch. At the first time, the progress was really slow. There is like 50 lines of MNIST loader code. We use pickle function to load the data, and separate it to training data and validation data. And we make the shape like (784, 1).

For such simple code, I reimplemented it for 5 times to finally grasp it. And then I try to implement the neural network part. 

