# 本地測試環境

需求
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions)
- [AWS SAM CLi](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [ngrok](https://ngrok.com/docs/getting-started)


1. 建立虛擬環境

  - Linux / MacOS
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r src/requirements.txt
    ```

  - Windows
    ```PowerShell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r src/requirements.txt
    ```

2. 確認 AWS 設定

```bash
aws sts get-caller-identity
```

  - 修改 AWS Profile (option)

    Linux / MacOS
    ```bash
    export AWS_PROFILE=myprofile
    aws sts get-caller-identity
    ```

  - Windows

    ```PowerShell
    $env:AWS_PROFILE="myprofile"
    aws sts get-caller-identity
    ```

3. 啟動本機 API

```bash
sam build --use-container
sam local start-api --env-vars .env.local.json
```

4. 建立 `ngrok` 轉發

```bash
ngrok http 3000 --host-header=rewrite
```

5. 到測試用 Line Account 設定 webhook
