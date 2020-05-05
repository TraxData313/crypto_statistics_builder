import json
import cbpro, time, datetime



def lambda_handler(event, context):
    public_client = cbpro.PublicClient()

    # - get the prices:
    current_value_LTC = public_client.get_product_ticker(product_id='LTC-USD')['price']
    current_value_ETH = public_client.get_product_ticker(product_id='ETH-USD')['price']
    current_value_BTC = public_client.get_product_ticker(product_id='BTC-USD')['price']
    print("- LTC price:", current_value_LTC)
    print("- ETH price:", current_value_ETH)
    print("- BTC price:", current_value_BTC)
    
    
    
    
    return_message = "LTC price: {}".format(current_value_LTC)
    return {
        'statusCode': 200,
        'body': return_message
    }
