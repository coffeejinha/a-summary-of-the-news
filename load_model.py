from transformers import BartForConditionalGeneration, PreTrainedTokenizerFast, pipeline

# KoBART 모델 로드
def load_kobart_summarizer():
    tokenizer = PreTrainedTokenizerFast.from_pretrained("gogamza/kobart-base-v2")
    model = BartForConditionalGeneration.from_pretrained("gogamza/kobart-base-v2")
    return pipeline("summarization", model=model, tokenizer=tokenizer, device=0)
