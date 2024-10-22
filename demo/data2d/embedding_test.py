import torch

emb = torch.nn.Embedding(num_embeddings=5,embedding_dim=3)

print(emb.weight)

input = torch.LongTensor([1])

print(input)

vec = emb(input)
print(vec)