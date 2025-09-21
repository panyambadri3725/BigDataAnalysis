# generate_data.py
# import os, random
#
# DATA_DIR = 'data'
# os.makedirs(DATA_DIR, exist_ok=True)
#
# for i in range(16):
#     with open(os.path.join(DATA_DIR, f'data{i}.txt'), 'w') as f:
#         for _ in range(1000):  # you can increase this to 1_500_000 for realistic test
#             nums = [str(random.randint(0, 100)) for _ in range(10)]  # 10 numbers per line
#             f.write(' '.join(nums) + '\n')
#
# print("✅ Sample data generated in ./data/")


# generate_data.py
import os
import random

DATA_DIR = os.path.join('.', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

for i in range(16):
    file_path = os.path.join(DATA_DIR, f'data{i}.txt')
    with open(file_path, 'w') as f:
        for _ in range(1000):  # use 1_500_000 for stress testing
            nums = [str(random.randint(0, 100)) for _ in range(10)]  # 10 numbers per line
            f.write(' '.join(nums) + '\n')

print(f"✅ Sample data generated in {DATA_DIR}")
