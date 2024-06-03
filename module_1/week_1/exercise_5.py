def md_nre_single_sample(y: float, y_hat: float, n: int, p: int):

    y_mean = y ** (1 / n)
    y_hat_mean = y_hat ** (1 / n)

    return abs(y_mean - y_hat_mean) ** p

if __name__ == "__main__":
    print(md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))
    print(md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1))
    print(md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1))
    print(md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1))
