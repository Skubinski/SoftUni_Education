bitcoin_to_bgn = 1168
yuan_to_dollar = 0.15
dollar_to_bgn = 1.76
euro_to_bgn = 1.95

# Въвеждане на стойностите от потребителя
bitcoin_amount = int(input())
yuan_amount = float(input())
commission = float(input())

# Пресмятане на стойностите в BGN
bitcoin_in_bgn = bitcoin_amount * bitcoin_to_bgn
yuan_in_dollar = yuan_amount * yuan_to_dollar
yuan_in_bgn = yuan_in_dollar * dollar_to_bgn

# Обща сума в BGN
total_in_bgn = bitcoin_in_bgn + yuan_in_bgn

# Пресмятане на комисионната
commission_amount = (commission / 100) * total_in_bgn

# Крайна сума в BGN след комисионната
final_amount = total_in_bgn - commission_amount

# Пресмятане на сумата в евро
euro_amount = final_amount / euro_to_bgn

# Извеждане на резултата
print(f"{euro_amount:.2f}")
