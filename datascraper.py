import playwright
import pandas as pd
import nest_asyncio
import asyncio
import time
import random
from playwright.async_api import async_playwright 

csv_path = "give_your_csv_path_that_has_appids"

df = pd.read_csv(csv_path)
df["Publisher Country"] = ""

async def get_publisher_country(playwright):
    browser = await playwright.chromium.launch(headless = False)
    context = await browser.new_context()
    page = await context.new_page()

    #to login manually

    await page.goto("https://app.sensortower.com/")

    print("Log in required, after logging in press enter here")
    input()

    for i, row in df.iterrows():
        app_id = row["appId"]
        app_url = f"https://app.sensortower.com/overview/{app_id}?country=US"
        print(f" Fetching: {app_url}")


        try:
            await page.goto(app_url, timeout=15000)
            await page.wait_for_selector("div:has-text('Publisher Country')", timeout=10000)

            country_element = await page.query_selector("text=Publisher Country")
            if country_element:
                country_value = await country_element.evaluate("el => el.nextElementSibling?.textContent || ''")
                country_value = country_value.strip()

                if country_value: 
                    df.at[i, "Publisher Country"] = country_value
                else:
                    df.at[i, "Publisher Country"] = "N/A"

        except Exception as e:
            print(f"error for an app {app_id} : {e} ")
            df.at[i, "Publisher Country"] = "Error"


        #random delay between fetches
        await asyncio.sleep(random.uniform(1.5, 3.5))

        # every 100 rows & save
        if (i + 1) % 100 == 0:
            print(f"Saving at row {i + 1}, taking short break...")
            df.to_csv(csv_path, index=False)
            time.sleep(15)


    await browser.close()


nest_asyncio.apply()
async def main():
    async with async_playwright() as playwright:
        await get_publisher_country(playwright)

await main()

df.to_csv(csv_path, index= False)
print("Task Done")





