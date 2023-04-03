# localchat

Based on https://medium.com/@mattesmattes/how-i-built-my-very-first-personal-chatbot-appliance-pca-powered-by-chatgpt-and-my-mac-mini-f6aeeedc7654

## Prepare

Setup docker

Add openai api key
cat $HOME/.openai.rc

```bash
# See https://platform.openai.com/account/api-keys
# See https://platform.openai.com/account/billing/limits
OPENAI_API_KEY=sk-Pfe...
```

## Run

```bash
make
```

## Create new model

```bash
rm data/index.json
```

Continue with "Run"
