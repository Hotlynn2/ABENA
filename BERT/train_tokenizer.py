from pathlib import Path

from tokenizers import BertWordPieceTokenizer

#paths = [str(x) for x in Path("./eo_data/").glob("**/*.txt")]
paths = ['jw300.en-tw.tw']

# Initialize a tokenizer
tokenizer = BertWordPieceTokenizer()

# Customize training
# And then train
tokenizer.train(
    paths,
    vocab_size=10000,
    min_frequency=2,
    show_progress=True,
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"],
    limit_alphabet=1000,
    wordpieces_prefix="##",
)

# Save files to disk
tokenizer.save("twibert")
