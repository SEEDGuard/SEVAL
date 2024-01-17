# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.
import argparse
from bleu import _bleu

def main():
    parser = argparse.ArgumentParser(description='Evaluate BLEU score and accuracy for code translation.')
    parser.add_argument('--actual', '-ref', required=True, help="reference translation filename, in txt format.")
    parser.add_argument('--predictions', '-pre', required=True, help="model's translations filename, in txt format.")
    args = parser.parse_args()

    with open(args.actual, 'r', encoding='utf-8') as ref_file, \
         open(args.predictions, 'r', encoding='utf-8') as pred_file:
        refs = ref_file.read().strip().splitlines()
        preds = pred_file.read().strip().splitlines()

    assert len(refs) == len(preds), "number of reference and prediction lines must be equal"

    correct_count = sum(r == p for r, p in zip(refs, preds))
    accuracy = correct_count / len(refs) * 100

    bleu_score = _bleu(args.actual, args.predictions)

    print(f'BLEU: {bleu_score:.2f}\nAccuracy: {accuracy:.2f}%')

if __name__ == '__main__':
    main()