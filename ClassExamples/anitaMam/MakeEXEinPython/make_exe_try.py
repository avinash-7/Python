import webbrowser

def main():
    print("Openning Favorite Sites")


with open('site.txt.txt', mode='rb') as fobj:
    try:
        for num, url in enumerate(fobj):
            webbrowser.open_new_tab(url.strip())
    except Exception as e:
        print(e)

    print("\nEnjoy!")

if __name__ == '__main__' : main()