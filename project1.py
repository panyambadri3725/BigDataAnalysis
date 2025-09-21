# # project1.py
# import os
# import json
# import sys
# from collections import Counter
# from multiprocessing import Pool
# from glob import glob
#
# # ---------- LOCAL CONFIG ----------
# DATA_DIR = './data/'
# OUTPUT_DIR = './output/'
# MAPPER_OUT_PREFIX = 'mapper_out_'
# REDUCER_OUT_FILE = 'reducer_output.json'
# NUM_MAPPERS = 4
# NUM_REDUCERS = 4
#
# os.makedirs(OUTPUT_DIR, exist_ok=True)
#
# # ---------- MAPPER ----------
# def mapper(file_path_outidx):
#     file_path, idx = file_path_outidx
#     counter = Counter()
#     with open(file_path, 'r') as f:
#         for line in f:
#             for num in map(int, line.strip().split()):
#                 counter[num] += 1
#
#     output_path = os.path.join(OUTPUT_DIR, f'{MAPPER_OUT_PREFIX}{idx}.json')
#     with open(output_path, 'w') as out:
#         json.dump(counter, out)
#
#     print(f"[Mapper-{idx}] Done: {output_path}")
#     return output_path
#
# # ---------- REDUCER ----------
# def reducer(file_list):
#     total_counter = Counter()
#     for file_path in file_list:
#         with open(file_path, 'r') as f:
#             counter = Counter(json.load(f))
#             total_counter += counter
#
#     top6 = total_counter.most_common(6)
#     result = {str(k): v for k, v in top6}
#
#     final_out_path = os.path.join(OUTPUT_DIR, REDUCER_OUT_FILE)
#     with open(final_out_path, 'w') as out:
#         json.dump(result, out, indent=2)
#
#     print(f"[Reducer] Done: {final_out_path}")
#     print("\nTop 6 Most Frequent Integers:")
#     for k, v in top6:
#         print(f"{k}: {v}")
#
# # ---------- MAIN ----------
# def main():
#     phase = sys.argv[1] if len(sys.argv) > 1 else 'all'
#     all_files = sorted(glob(os.path.join(DATA_DIR, 'data*.txt')))
#     file_chunks = [all_files[i::NUM_MAPPERS] for i in range(NUM_MAPPERS)]
#     mapper_args = [(f, i*len(chunk)+j) for i, chunk in enumerate(file_chunks) for j, f in enumerate(chunk)]
#
#     if phase == 'mapper':
#         print(f"[Main] Running {NUM_MAPPERS} mappers...")
#         with Pool(processes=NUM_MAPPERS) as pool:
#             mapper_outputs = pool.map(mapper, mapper_args)
#         return
#
#     elif phase == 'reducer':
#         print("[Main] Running reducer...")
#         mapper_outputs = sorted(glob(os.path.join(OUTPUT_DIR, f'{MAPPER_OUT_PREFIX}*.json')))
#         reducer(mapper_outputs)
#         return
#
#     else:
#         print("[Main] Invalid argument. Use 'mapper' or 'reducer'.")
#
# if __name__ == '__main__':
#     main()


# project1.py
import os
import json
import sys
from collections import Counter
from multiprocessing import Pool
from glob import glob

# ---------- LOCAL CONFIG ----------
DATA_DIR = os.path.join('.', 'data')
OUTPUT_DIR = os.path.join('.', 'output')
MAPPER_OUT_PREFIX = 'mapper_out_'
REDUCER_OUT_FILE = 'reducer_output.json'
NUM_MAPPERS = 4
NUM_REDUCERS = 4

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- MAPPER ----------
def mapper(file_path_outidx):
    file_path, idx = file_path_outidx
    counter = Counter()
    with open(file_path, 'r') as f:
        for line in f:
            for num in map(int, line.strip().split()):
                counter[num] += 1

    output_path = os.path.join(OUTPUT_DIR, f'{MAPPER_OUT_PREFIX}{idx}.json')
    with open(output_path, 'w') as out:
        json.dump(counter, out)

    print(f"[Mapper-{idx}] Done: {output_path}")
    return output_path

# ---------- REDUCER ----------
def reducer(file_list):
    total_counter = Counter()
    for file_path in file_list:
        with open(file_path, 'r') as f:
            counter = Counter(json.load(f))
            total_counter += counter

    top6 = total_counter.most_common(6)
    result = {str(k): v for k, v in top6}

    final_out_path = os.path.join(OUTPUT_DIR, REDUCER_OUT_FILE)
    with open(final_out_path, 'w') as out:
        json.dump(result, out, indent=2)

    print(f"[Reducer] Done: {final_out_path}")
    print("\nTop 6 Most Frequent Integers:")
    for k, v in top6:
        print(f"{k}: {v}")

# ---------- MAIN ----------
def main():
    phase = sys.argv[1] if len(sys.argv) > 1 else 'all'
    all_files = sorted(glob(os.path.join(DATA_DIR, 'data*.txt')))
    file_chunks = [all_files[i::NUM_MAPPERS] for i in range(NUM_MAPPERS)]
    mapper_args = [(f, i * len(chunk) + j) for i, chunk in enumerate(file_chunks) for j, f in enumerate(chunk)]

    if phase == 'mapper':
        print(f"[Main] Running {NUM_MAPPERS} mappers...")
        with Pool(processes=NUM_MAPPERS) as pool:
            mapper_outputs = pool.map(mapper, mapper_args)
        return

    elif phase == 'reducer':
        print("[Main] Running reducer...")
        mapper_outputs = sorted(glob(os.path.join(OUTPUT_DIR, f'{MAPPER_OUT_PREFIX}*.json')))
        reducer(mapper_outputs)
        return

    else:
        print("[Main] Invalid argument. Use 'mapper' or 'reducer'.")

if __name__ == '__main__':
    main()
