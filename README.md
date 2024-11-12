# UTMN assistant

## RUN command

shell
```shell
docker build -t utmn .
docker run --env-file ./.env-local  -t utmn
```

bash
```bash
docker build -t utmn . && docker run --env-file ./.env-local  -t utmn
```