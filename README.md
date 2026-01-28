# vLLM Helm Chart

## Usage
~~~bash
# Install vllm deployment 
helm install vllm ./chart -n vllm --create-namespace

# Create "testing ubuntu" pod
kubectl apply -f testing-ubuntu.yaml
~~~

Open testing shell in `testing-ubuntu` pod and run testing commands:
~~~bash
curl http://vllm-server.vllm:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{"prompt": "San Francisco is a",
       "max_tokens": 30,
       "temperature": 0}' | jq
~~~

Expected response:
~~~json
{
  "id": "cmpl-b5c2c24b7b8a184b",
  "object": "text_completion",
  "created": 1769612130,
  "model": "HuggingFaceTB/SmolLM2-135M",
  "choices": [
    {
      "index": 0,
      "text": " city of 1.5 million people, and it is the second largest city in the United States. It is located in the San Francisco Bay Area",
      "logprobs": null,
      "finish_reason": "length",
      "stop_reason": null,
      "token_ids": null,
      "prompt_logprobs": null,
      "prompt_token_ids": null
    }
  ],
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "prompt_tokens": 4,
    "total_tokens": 34,
    "completion_tokens": 30,
    "prompt_tokens_details": null
  },
  "kv_transfer_params": null
}
~~~
