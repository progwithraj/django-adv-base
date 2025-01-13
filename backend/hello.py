from collections import ChainMap


def main():
    default_pref: dict[str, str | int | bool] = {
        "lang": "en",
        "theme": "light",
        "notifications": True,
        "value": 10,
    }

    user_pref: dict[str, str | int | bool] = {
        "theme": "dark",
        "notifications": False,
        "value": 20,
    }

    merged_pref: ChainMap[str, str | bool | int] = ChainMap(user_pref, default_pref)
    #    user_pref['theme'] = 'light'
    #    print(merged_pref['theme'])
    print("actual", merged_pref.maps[1])
    merged_pref.update(abob=34)
    print("updated", merged_pref)


if __name__ == "__main__":
    main()
