import os.path
import pytest
from selene import browser, be, have

def test_student_registration_form():
    browser.open('/')
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.6)"')
    browser.element('#RightSide_Advertisement').execute_script('element.remove()')

    browser.element('#firstName').should(be.blank).type('Kirill')
    browser.element('#lastName').should(be.blank).type('Adamenkov')
    browser.element('#userEmail').should(be.blank).type('i@kiruix.ru')

    browser.element('[for="gender-radio-1"]').should(have.exact_text('Male')).click()
    browser.all('#genterWrapper .col-md-9>div').should(have.size(3))

    browser.element('#userNumber').should(be.blank).type('89999999999')

    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    browser.element('.react-datepicker__month-select [value="8"]').should(be.clickable).click()
    browser.element('.react-datepicker__year-select [value="1996"]').should(be.clickable).click()
    browser.element('[aria-label="Choose Monday, September 9th, 1996"].react-datepicker__day--009').should(be.clickable).click()
    browser.element('#dateOfBirthInput').should(have.value('09 Sep 1996'))

    browser.element('#subjectsInput').should(be.blank).type('math')
    browser.element('#react-select-2-option-0').click()
    browser.element('.subjects-auto-complete__multi-value__label').should(have.text('Maths'))

    browser.all('#hobbiesWrapper .col-md-9.col-sm-12>div').should(have.size(3))
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture.form-control-file').send_keys(os.path.abspath('1.png'))

    browser.element('#currentAddress').should(be.blank).click().type('Moscow, Russia')

    browser.element('#state').should(have.text('Select State')).click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#state').should(have.text('Uttar Pradesh'))

    browser.element('#city').should(have.text('Select City')).click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#city').should(have.text('Lucknow'))

    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-child(2)').should(have.texts(
        'Kirill Adamenkov',
        'i@kiruix.ru',
        'Male',
        '8999999999',
        '09 September,1996',
        'Maths',
        'Sports, Music',
        '1.png',
        'Moscow, Russia',
        'Uttar Pradesh Lucknow'
    ))