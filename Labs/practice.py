
copy = ['English', 'Danish', 'Dutch', 'Finnish', 'French', 'German', 'Indonesian', 'Italian', 'Japanese', 'Latin', 'Norwegian', 'Portuguese', 'Spanish', 'Swahili', 'Swedish']

i = 0
copy.remove("English")
for language in copy:
    if i == 7:
        print("\t")
        print(language, end=" ")
    else:
        print(language, end=" ")
    i +=1