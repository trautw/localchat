FROM python
RUN pip install openai gpt_index mailbox unicode html2text unidecode gradio 
WORKDIR /root
COPY genmodel.py genmodel.py
COPY serve.py serve.py
