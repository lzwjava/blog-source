---
title: C++ Compilation Error Missing Python.h
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
model: x-ai/grok-4-fast
---

raise exc.CppCompileError(cmd, output) from e
torch._inductor.exc.InductorError: CppCompileError: C++ compile error

Command:
g++ /tmp/torchinductor_lzwjava/xy/cxyve26btthvhcuhmj6fjdn6e6op2ypybj7jmfcjx275gxkffhg5.cpp -D TORCH_INDUCTOR_CPP_WRAPPER -D STANDALONE_TORCH_HEADER -D C10_USING_CUSTOM_GENERATED_MACROS -D CPU_CAPABILITY_AVX2 -shared -fPIC -O3 -DNDEBUG -fno-trapping-math -funsafe-math-optimizations -ffinite-math-only -fno-signed-zeros -fno-math-errno -fexcess-precision=fast -fno-finite-math-only -fno-unsafe-math-optimizations -ffp-contract=off -fno-tree-loop-vectorize -march=native -Wall -std=c++17 -Wno-unused-variable -Wno-unknown-pragmas -fopenmp -I/usr/include/python3.13 -I/home/lzwjava/.local/lib/python3.13/site-packages/torch/include -I/home/lzwjava/.local/lib/python3.13/site-packages/torch/include/torch/csrc/api/include -mavx2 -mfma -mf16c -D_GLIBCXX_USE_CXX11_ABI=1 -ltorch -ltorch_cpu -ltorch_python -lgomp -L/usr/lib/x86_64-linux-gnu -L/home/lzwjava/.local/lib/python3.13/site-packages/torch/lib -o /tmp/torchinductor_lzwjava/xy/cxyve26btthvhcuhmj6fjdn6e6op2ypybj7jmfcjx275gxkffhg5.so

Output:
/tmp/torchinductor_lzwjava/xy/cxyve26btthvhcuhmj6fjdn6e6op2ypybj7jmfcjx275gxkffhg5.cpp:94:10: fatal error: Python.h: No such file or directory
   94 | #include <Python.h>
      |          ^~~~~~~~~~
compilation terminated.


Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"