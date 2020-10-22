import rsa
import basic_algorithms

def gen_c(len_keys,p):
    while True:
        c = rsa.generation_prime_numb(len_keys)
        if basic_algorithms.gcd(c, p-1) == 1 and c<p:
            break
    return c

def text_to_blocks_num(text,len_keys):
    len_block = (len_keys // 4) -1
    blocks = [text[i:i + len_block] for i in range(0, len(text), len_block)]
    for i in range(len(blocks)):
        blocks[i] = rsa.text_in_numb(blocks[i])
    return blocks

def generation_c_and_d(p,len_keys):
    while True:
        c = rsa.generation_prime_numb(len_keys)
        if basic_algorithms.gcd(c, p-1) == 1 and c < p:
            break
    d = basic_algorithms.invert(c, p - 1)
    return c,d

def send_block(block,c_a,d_a,c_b,d_b,p):
    x1 = basic_algorithms.modular_pow(block, c_a, p)
    x2 = basic_algorithms.modular_pow(x1, c_b, p)
    x3 = basic_algorithms.modular_pow(x2, d_a, p)
    x4 = basic_algorithms.modular_pow(x3, d_b, p)
    return x1,x2,x3,x4

def blocks_num_to_text(blocks,len_keys):
    for i in range(len(blocks)):
        blocks[i] = blocks[i].rjust((((len_keys//4)-1)*4),'0')
    print(blocks)
    result = ''.join(blocks)
    result_text = ''
    for i in range(len(result) // 4):
        var = int(result[i * 4:(i + 1) * 4])
        if var != 0:
            result_text += chr(var)
    return result_text



'''
text = 123
len_keys = 50
p = rsa.generation_prime_numb(len_keys)
print("p = " + str(p))

while True:
    c_a = gen_c(len_keys, p)
    d_a = rsa.generation_prime_numb(len_keys)
    d_a = basic_algorithms.invert(c_a,p-1)
    if d_a>0 and d_a<p and basic_algorithms.gcd(c_a*d_a,p-1):
        break

print("c_a = " + str(c_a))
print("d_a = " + str(d_a))
while True:
    c_b = gen_c(len_keys, p)
    d_b = rsa.generation_prime_numb(len_keys)
    d_b = basic_algorithms.invert(c_b,p-1)
    if d_b>0 and d_b<p and basic_algorithms.gcd(c_b*d_b,p-1):
        break

print("c_b = " + str(c_b))
print("d_b = " + str(d_b))


x1 = basic_algorithms.modular_pow(text,c_a,p)
x2 = basic_algorithms.modular_pow(x1,c_b,p)
x3 = basic_algorithms.modular_pow(x2,d_a,p)
x4 = basic_algorithms.modular_pow(x3,d_b,p)
print("x1 = " + str(x1))
print("x2 = " + str(x2))
print("x3 = " + str(x3))
print("x4 = " + str(x4))
'''