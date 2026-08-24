class PersonalizedBeautySubscriptionBoxRecommenderClient:
    def curate_glam_bag(self, skin_tone='medium_olive', eye_color='hazel', makeup_style='clean_girl_glow'):
        products = [
            {'brand': 'Tatcha', 'item': 'Dewy Skin Cream Deluxe', 'category': 'skincare', 'value_usd': 24.0},
            {'brand': 'Rare Beauty', 'item': 'Soft Pinch Liquid Blush (Hope)', 'category': 'makeup', 'value_usd': 23.0},
            {'brand': 'Tower 28', 'item': 'ShineOn Jelly Lip Gloss', 'category': 'lips', 'value_usd': 16.0},
            {'brand': 'Olaplex', 'item': 'No. 3 Hair Perfector Travel', 'category': 'haircare', 'value_usd': 15.0},
            {'brand': 'Glow Recipe', 'item': 'Watermelon Niacinamide Dew Drops', 'category': 'serum', 'value_usd': 20.0}
        ]
        return {
            'curated_bag_id': 'ips_bag_9021',
            'subscriber_profile': {'tone': skin_tone, 'eyes': eye_color, 'style': makeup_style},
            'box_products': products,
            'total_retail_value_usd': sum(p['value_usd'] for p in products),
            'monthly_subscription_price_usd': 14.0,
            'custom_choice_item_selected': 'Rare Beauty Soft Pinch Liquid Blush'
        }
