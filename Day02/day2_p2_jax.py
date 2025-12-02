import sys

import jax
import jax.numpy as jnp

from jax import lax
from jax import jit, vmap

jax.config.update("jax_enable_x64", True)


def is_made_of_repeated_seq_of_len(x, n):
    x, seq = divmod(x, 10**n)
    def cond_func(v): return v % 10**n == seq
    def body_func(v): return v // 10**n
    return lax.while_loop(cond_func, body_func, x) == 0


@jit
@vmap
def is_invalid_id(x):
    xlen = jnp.log10(x).astype(int) + 1
    return lax.fori_loop(
        1, xlen // 2 + 1,
        lambda i, v: lax.cond(
            v,
            lambda _: True,
            lambda _: is_made_of_repeated_seq_of_len(x, i),
            None
        ),
        False
    )


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} <input.txt>')
        exit(0)

    with open(sys.argv[1], 'r') as f:
        contents = f.read().strip().split(',')

    invalid_ids = set()
    for rng in contents:
        rng = rng.split('-')
        ids = jnp.arange(int(rng[0]), int(rng[1]) + 1, dtype=jnp.uint64)
        id_labels = is_invalid_id(ids)
        ids = ids * id_labels
        id_labels = jnp.nonzero(ids)
        for i in ids[id_labels]:
            invalid_ids.add(int(i))
        # print(f'For range {rng}, there are {jnp.sum(id_labels)} many invalid labels.')

    # print(invalid_ids)
    print(f'Sum of invalid ids: {sum(invalid_ids)}')
