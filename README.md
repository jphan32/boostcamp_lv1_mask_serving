# Streamlit

## 환경 설정

```
virtualenv --python=python3 mask_serving
source mask_serving/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Streamlit Port 설정 / Streamlit Email 설정
~/.streamlit/config.toml
```
[server]
address = "0.0.0.0"
port = 32110
maxUploadSize = 5

[theme]
base = "light"
```

~/.streamlit/credentials.toml
```
[general]
email = "YOUR_EMAIL_ADDRESS"
```

## Streamlit 실행
```
./run_server.sh
```

## Streamlit Log 확인
```
tail -f /var/log/streamlit.log
```