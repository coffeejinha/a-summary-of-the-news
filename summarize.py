def split_text(text, max_length=1024):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length > max_length:
            chunks.append('. '.join(current_chunk) + '.')
            current_chunk = [sentence]
            current_length = sentence_length
        else:
            current_chunk.append(sentence)
            current_length += sentence_length

    if current_chunk:
        chunks.append('. '.join(current_chunk) + '.')

    return chunks

def summarize_large_text(summarizer, text, max_length=250, min_length=30):
    chunks = split_text(text)
    summaries = []

    for i, chunk in enumerate(chunks):
        print(f"요약 중 ({i+1}/{len(chunks)})...")
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    return " ".join(summaries)
