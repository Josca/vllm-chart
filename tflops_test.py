import torch
import time

# Make sure you're on ROCm
assert torch.version.hip is not None

device = "cuda"

M = N = K = 2**14

# dtype = torch.float32 # FP32 (Vector)
dtype = torch.float64 # FP64 (Vector)

A = torch.randn((M, K), device=device, dtype=dtype)
B = torch.randn((K, N), device=device, dtype=dtype)

# Warmup
for _ in range(10):
    C = torch.matmul(A, B)

torch.cuda.synchronize()

# Timed runs
iters = 20
start = time.time()
for _ in range(iters):
    C = torch.matmul(A, B)

torch.cuda.synchronize()
elapsed = time.time() - start

# FLOPs calculation
flops = 2 * M * N * K * iters
tflops = flops / elapsed / 1e12

print(f"Elapsed time: {elapsed:.3f} s")
print(f"GEMM Throughput: {tflops:.1f} TFLOPs")
