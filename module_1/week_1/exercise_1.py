def exercise1(tp, fp, fn):

    dict_map = {"tp": tp,
                "fp": fp,
                "fn": fn}

    for key, value in dict_map.items():

        if not isinstance(value, int):
            print(f"{key} must be int")
            return

        if value <= 0:
            print(f"{key} must be greater than 0")
            return

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)

    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"precision is {2*precision*recall/(precision+recall)}")

if __name__ == "__main__":
    exercise1( tp =2  , fp =3 , fn =4)
    exercise1( tp ='a', fp =3 , fn =4)
    exercise1( tp =2 , fp ='a', fn =4)
    exercise1( tp =2 , fp =3 , fn ='a')
    exercise1( tp =2 , fp =3 , fn =0)
    exercise1( tp =2.1 , fp =3 , fn =0)