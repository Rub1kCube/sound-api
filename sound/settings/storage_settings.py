from sound.settings.env_reader import env


# S3 compatible storage credentials.
AWS_S3_ENDPOINT_URL = env.str('MINIO_ENDPOINT')
AWS_ACCESS_KEY_ID = env.str('MINIO_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = env.str('MINIO_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = env.str('MINIO_BUCKET_NAME', 'sound-public-bucket')
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
