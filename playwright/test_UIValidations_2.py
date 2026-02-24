import time

from playwright.sync_api import Page, expect


## Placeholers and Hide/display
def test_UICehcks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(2)
    ### non html java alert popups
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    ## Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Reload").click()


    ######### Frame Handling
    framepage = page.frame_locator("#courses-iframe")
    framepage.get_by_role("link", name="All Access plan").click()
    expect(framepage.locator("body")).to_contain_text("Happy Subscibers!")
    time.sleep(3)

    ##### Check the price of rice is equal to 37
    ### Identify the price column
    ### Identify the rice row
    ### Extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColoumn=index
            print(f"Price coloumn has value {priceColoumn}")
            break

    riceRowValue = page.locator("tr").filter(has_text='Rice')
    #print(f"Rice row value is : {riceRowValue}")
    expect(riceRowValue.locator("td").nth(priceColoumn)).to_have_text("37")









