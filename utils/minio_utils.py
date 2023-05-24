from minio import Minio

from conf.default import BaseConfig
import datetime
import logging
import os
import io


def upload_file_to_minio(key_name, file_path=""):
    """
        上传文件到 minio
    """
    minio_client = Minio(BaseConfig.MinIO_IP_PORT, access_key=BaseConfig.MinIO_ACCESS_KEY,
                         secret_key=BaseConfig.MinIO_SECRET_KEY, secure=BaseConfig.MinIO_SECURE)
    minio_client.fput_object(BaseConfig.BUCKET_NAME, key_name, file_path)


def download_file_from_minio(key_name, file_path=""):
    """
    下载文件从minio
    """
    minio_client = Minio(BaseConfig.MinIO_IP_PORT, access_key=BaseConfig.MinIO_ACCESS_KEY,
                         secret_key=BaseConfig.MinIO_SECRET_KEY, secure=BaseConfig.MinIO_SECURE)
    return minio_client.fget_object(BaseConfig.BUCKET_NAME, key_name, file_path)


def generate_file_temporary_url(key_name, endpoint=None, bucket_name=None):
    """
        生成文件临时　url
    """
    if endpoint is None:
        endpoint = BaseConfig.MinIO_IP_PORT
    if bucket_name is None:
        bucket_name = BaseConfig.BUCKET_NAME
    minio_client = Minio(endpoint, access_key=BaseConfig.MinIO_ACCESS_KEY,
                         secret_key=BaseConfig.MinIO_SECRET_KEY, secure=BaseConfig.MinIO_SECURE)
    sign_url = minio_client.presigned_get_object(
        bucket_name, key_name, expires=datetime.timedelta(days=7))
    return sign_url


def upload_file2minio(key_name, data_type="file", data="", file_path=""):
    success = False
    msg = ""
    minio_client = Minio(BaseConfig.MinIO_IP_PORT, access_key=BaseConfig.MinIO_ACCESS_KEY,
                         secret_key=BaseConfig.MinIO_SECRET_KEY, secure=BaseConfig.MinIO_SECURE)
    if data_type == "file":
        if file_path == "":
            return False, "require file path"
        if not os.path.exists(file_path):
            return False, "file not exists"
        try:
            minio_client.fput_object(BaseConfig.BUCKET_NAME, key_name, file_path)
            success = True
        except Exception as e:
            msg = "upload file fail"
            logging.exception(e)
        return success, msg
    elif data_type == "binary":
        file_size = len(data)
    elif data_type == "string":
        data_as_bytes = data.encode('utf-8')
        file_size = len(data_as_bytes)
        data = io.BytesIO(data_as_bytes)
    else:
        return success, "data type not allow"
    try:
        minio_client.put_object(BaseConfig.BUCKET_NAME, key_name, data, file_size)
        success = True
    except Exception as e:
        msg = "upload file fail"
        logging.exception(e)
    return success, msg