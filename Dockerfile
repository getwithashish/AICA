# FROM vllm/vllm-openai:latest
FROM pytorch/pytorch:latest

RUN pip install vllm

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install nginx -y

# RUN mkdir -p /home/chatbot/ssl/certs
# COPY certificate.crt /home/chatbot/ssl/certs/certificate.crt
# COPY private.key /home/chatbot/ssl/certs/private.key

# COPY nginx.conf /etc/nginx/nginx.conf
# RUN nginx -t
# RUN service nginx restart

RUN python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8888 --max-logprobs 2 --model getwithashish/phi3-mini-internal-dept-model-merged
