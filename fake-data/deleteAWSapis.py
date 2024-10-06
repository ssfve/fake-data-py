import time

import boto3


def delete_apis():
    # 创建一个 boto3 客户端来连接到 API Gateway
    client = boto3.client('apigateway')

    # 获取所有 API Gateway 的列表
    response = client.get_rest_apis()
    apis = response['items']

    # 遍历每个 API 并删除
    for api in apis:
        # 跳过名为 'name' 的 API，如果需要删除特定命名规则的 API，请修改此处逻辑
        if api['name'] != 'specific_name_to_skip':
            try:
                # 删除 API
                client.delete_rest_api(restApiId=api['id'])
                print(f"Deleted API: {api['name']} with ID: {api['id']}")
            except Exception as e:
                # 捕获并打印任何可能发生的错误
                print(f"Failed to delete API: {api['name']} with ID: {api['id']}. Error: {e}")

            # 在每次删除后等待 30 秒
            time.sleep(30)


if __name__ == "__main__":
    for i in range(20):
        delete_apis()
