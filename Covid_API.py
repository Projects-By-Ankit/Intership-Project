import requests

from tkinter import *


def getdata():
    try:
        c_name = city_entry.get()

        api = "https://disease.sh/v3/covid-19/countries/" + c_name + "?strict=true"
        data = requests.get(api).json()
        total_pop = Label(text=data["population"], font="bold")
        total_pop.grid(row=2, column=1)
        con_case = Label(text=data["cases"], font="bold")
        con_case.grid(row=3, column=1)
        recovered_cases = Label(text=data["recovered"], font="bold")
        recovered_cases.grid(row=4, column=1)
        death_case = Label(text=data["deaths"], font="bold")
        death_case.grid(row=5, column=1)
        act_case = Label(text=data["active"], font="bold")
        act_case.grid(row=6, column=1)
        today_case = Label(text=data["todayCases"], font="bold")
        today_case.grid(row=7, column=1)
        death_today_case = Label(text=data["todayDeaths"], font="bold")
        death_today_case.grid(row=8, column=1)

    except Exception as e:
        print(e)


root = Tk()
root.title("----Covid Tracking Software----")
root.geometry("350x250")
root.minsize(350, 250)
root.maxsize(350, 250)

label_country = Label(text="Enter Country Name:", font="bold")
label_country.grid(row=1, column=0)
city_entry = Entry()
city_entry.grid(row=1, column=1)

label_population = Label(text="Total Population:", font="bold")
label_population.grid(row=2, column=0)
label_confirmed_case = Label(text="Confirmed Cases:", font="bold")
label_confirmed_case.grid(row=3, column=0)
label_recover_case = Label(text="Recovered Cases:", font="bold")
label_recover_case.grid(row=4, column=0)
label_death_case = Label(text="Death Cases:", font="bold")
label_death_case.grid(row=5, column=0)
label_active_case = Label(text="Active Cases:", font="bold")
label_active_case.grid(row=6, column=0)
label_case_per_mil = Label(text="Today Cases:", font="bold")
label_case_per_mil.grid(row=7, column=0)
label_death_per_mil = Label(text="Today Deaths:", font="bold")
label_death_per_mil.grid(row=8, column=0)

Button(text="Submit", command=getdata).grid(row=9, column=1)

root.mainloop()
