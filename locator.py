class Homepage:
    base_url = "http://edspert.id/"
    tentang_url = "http://edspert.id/pages/tentang-kami"
    google_auth = "https://accounts.google.com/o/oauth2"
    all_class_url = "http://edspert.id/pages/all-class"

class Navbar:
    logo = "#main-wrapper > nav > a > img"
    menu_program = '#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu:nth-child(1)'
    menu_bidang_ilmu = '#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu:nth-child(2)'
    menu_tentang = '#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu:nth-child(3)'

    login_button = '#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.btn-orange.m-login.submenu'

    menu_program_items = "#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu.show > div > div"
    program_webinar = "#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu.show > div > div > div:nth-child(1) > div.col-2"
    program_bootcamp = "#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu.show > div > div > div:nth-child(2) > div.col-2"
    program_online_course = "#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu.show > div > div > div:nth-child(3) > div.col-2"

    menu_bidang_ilmu_items = "#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu.show > div > div"
    program_tech_development = "#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu.show > div > div > div:nth-child(1) > div.col-2"
    program_data = "#navbarSupportedContent > ul.navbar-nav.ml-auto.desktop > li.nav-item.dropdown.submenu.show > div > div > div:nth-child(2) > div.col-2"

    login_modal = "#login > div"
    login_link = "#registermodal > div > div > div > a"


class Hero:
    title = "#main-wrapper > div.image-cover.hero_banner > div > div.row.align-items-center.banner-homepage > div > div > div > div.dtl-banner"
    subtitle = "#main-wrapper > div.image-cover.hero_banner > div > div.row.align-items-center.banner-homepage > div > div > div > div.subdtl-banner" 
    jelajahi_kelas_button = "#main-wrapper > div.image-cover.hero_banner > div > div.row.align-items-center.banner-homepage > div > div > div > div.pt-4 > a"


class Section1:
    title = "#main-wrapper > section.reason > div.t-reason"
    subtitle = "#main-wrapper > section.reason > div.st-reason"
    card_item = "#main-wrapper > section.reason > div.row > div.col-lg-3.col-sm-12.col-md-6.card-reason"
    card_1 = "#main-wrapper > section.reason > div.row > div.col-lg-3.col-sm-12.col-md-6.card-reason:nth-child(1)"
    card_2 = "#main-wrapper > section.reason > div.row > div.col-lg-3.col-sm-12.col-md-6.card-reason:nth-child(2)"
    card_3 = "#main-wrapper > section.reason > div.row > div.col-lg-3.col-sm-12.col-md-6.card-reason:nth-child(3)"
    card_4 = "#main-wrapper > section.reason > div.row > div.col-lg-3.col-sm-12.col-md-6.card-reason:nth-child(4)"

    card_1_title = "#main-wrapper > section.reason > div.row > div:nth-child(1) > div.txt-reason.m-t-64"
    card_1_subtitle = "#main-wrapper > section.reason > div.row > div:nth-child(1) > div.subtxt-reason"
    
    card_2_title = "#main-wrapper > section.reason > div.row > div:nth-child(2) > div.txt-reason.m-t-64"
    card_2_subtitle = "#main-wrapper > section.reason > div.row > div:nth-child(2) > div.subtxt-reason"
    
    card_3_title = "#main-wrapper > section.reason > div.row > div:nth-child(3) > div.txt-reason.m-t-82"
    card_3_subtitle = "#main-wrapper > section.reason > div.row > div:nth-child(3) > div.subtxt-reason"
    
    card_4_title = "#main-wrapper > section.reason > div.row > div:nth-child(4) > div.txt-reason.m-t-82"
    card_4_subtitle = "#main-wrapper > section.reason > div.row > div:nth-child(4) > div.subtxt-reason"

class Section2:
    title = "#main-wrapper > section.program > div.t-program"
    subtitle = "#main-wrapper > section.program > div.st-program"
    card_item = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div.col-lg-4.col-md-12.col-sm-12.card-program.slick-slide.slick-active"
    card_1 = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div.col-lg-4.col-md-12.col-sm-12.card-program.slick-slide.slick-active[describedby='slick-slide20']"
    card_2 = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div.col-lg-4.col-md-12.col-sm-12.card-program.slick-slide.slick-active[describedby='slick-slide21']"
    card_3 = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div.col-lg-4.col-md-12.col-sm-12.card-program.slick-slide.slick-active[describedby='slick-slide22']"

    card_1_title = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div:nth-child(1) > div.txt-program > div"
    card_1_desc = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div:nth-child(1) > div.subtxt-program.mmt-0"

    card_2_title = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div:nth-child(2) > div.txt-program > div"
    card_2_desc = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div:nth-child(2) > div.subtxt-program.mmt-0"

    card_3_title = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div:nth-child(3) > div.txt-program > div"
    card_3_desc = "#main-wrapper > section.program > div.row.w-100.nav-programs.slick-initialized.slick-slider > div > div > div:nth-child(3) > div.subtxt-program.mmt-0"