import pandas as pd
import matplotlib.pyplot as plt

def characters_in_yr(csv1, csv2, yr_column):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    #remove *C denoting cameos
    for col in df1.select_dtypes(include=['object']).columns:
        df1[col] = df1[col].str.strip(' *C')

    #remove extra asterisks that got added when i ripped the episodes from the wiki
    for col in df2.select_dtypes(include=['object']).columns:
        df2[col] = df2[col].str.strip(' *')

    #dictionary to store characters if their array isn't empty
    characters_in_yr = []

    #tolist() function in NumPy converts an array into a nested Python list and returns it.
    #Each element in the array is converted into the closest compatible built-in Python type using the .item() function.
    yr_cartoons = df2[yr_column].dropna().tolist()

    for character in df1.columns:
        chr_appears = df1[character].dropna().tolist()

        #check for common items
        common_items = [cartoon for cartoon in chr_appears if cartoon in yr_cartoons]

        #if the character's array of episodes for a given year isn't empty append character
        if common_items:
            characters_in_yr.append(character)

    return characters_in_yr

def characters_by_yr(csv1, csv2):
    df2 = pd.read_csv(csv2)

    character_counts_by_yr = []

    for yr_column in df2.columns:
        all_chars = characters_in_yr(csv1, csv2, yr_column)
        count_chars = len(all_chars)
        character_counts_by_yr.append(count_chars)
        #character_string = ', '.join(map(str, all_chars)).title()
        #print(f"Characters appearing in {yr_column}: {count_chars} ({character_string})")

    return character_counts_by_yr

def get_yrs(csv2):
    df2 = pd.read_csv(csv2, header=None)

    for col in df2.select_dtypes(include=['object']).columns:
        df2[col] = df2[col].str.strip('Y_')

    all_yrs = []

    for year in df2.columns:
        years_in_csv = df2[year].iloc[0]
        all_yrs.append(years_in_csv)

    return all_yrs

csv1 = '1944-1964 - CHARACTERS.csv'
csv2 = '1944-1964 - YEARS.csv'

years_for_df3 = get_yrs(csv2)
character_counts = characters_by_yr(csv1, csv2)

print(f"{character_counts}")
#print(f"{years_for_df3}")

df3 = pd.DataFrame(character_counts, years_for_df3).transpose()

print(df3)
df3.plot()
bar_plot = plt.bar(x = years_for_df3, height = character_counts)
plt.bar_label(bar_plot, labels = character_counts)
plt.legend([])
plt.show()