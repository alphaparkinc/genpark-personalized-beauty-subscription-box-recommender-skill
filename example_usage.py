from client import PersonalizedBeautySubscriptionBoxRecommenderClient

def main():
    client = PersonalizedBeautySubscriptionBoxRecommenderClient()
    res = client.curate_glam_bag('light_warm', 'brown', 'dewy_minimalist')
    print('Bag: ' + res['curated_bag_id'] + ' | Total Value: $' + str(res['total_retail_value_usd']) + ' for $' + str(res['monthly_subscription_price_usd']))
    print('Choice Item: ' + res['custom_choice_item_selected'])
    for p in res['box_products']:
        print('  - ' + p['brand'] + ' ' + p['item'] + ' ($' + str(p['value_usd']) + ')')

if __name__ == '__main__':
    main()
