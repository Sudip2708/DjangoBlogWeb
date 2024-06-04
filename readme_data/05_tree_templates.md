### Souborová struktura šablon projektu

    ├─ templates

###### Základní šablona pro všechny stránky projektu

    │  ├─ 0_base
    │  │  ├─ 00__base__.html
    │  │  ├─ 01__head__.html
    │  │  ├─ 02__header__.html
    │  │  ├─ 03__messages__.html
    │  │  ├─ 04__footer__.html
    │  │  ├─ 05__body_scripts__.html
    │  │  ├─ _footer
    │  │  │  ├─ __content__.html
    │  │  │  ├─ __edit_section__.html
    │  │  │  ├─ __end_line_section__.html
    │  │  │  ├─ _content_data
    │  │  │	 │	├─ _address_and_social_.html
    │  │  │	 │	├─ _articles_.html
    │  │  │	 │	└─ _selected_links_.html
    │  │  │	 └─ _edit_data
    │  │  │		├─ _column_1_.html
    │  │  │		├─ _column_2_.html
    │  │  │		├─ _column_3_.html
    │  │  │		└─ _column_4_.html
    │  │  ├─ _head
    │  │  │  ├─ __links__.html
    │  │  │  ├─ __meta__.html
    │  │  │  └─ __scripts__.html
    │  │  └─ _header
    │  │	 ├─ __dropdown_display__.html
    │  │	 ├─ __navigation__.html
    │  │	 ├─ _dropdown_data
    │  │	 │	├─ __dropdown_menu__.html
    │  │	 │	├─ _button_.html
    │  │	 │	├─ _category_dropdown_.html
    │  │	 │	├─ _create_article_and_favorite_.html
    │  │	 │	├─ _homepage_articles_search_.html
    │  │	 │	├─ _profile_and_login_.html
    │  │	 │	├─ _show_sidebar_.html
    │  │	 │	└─ _special_offer_.html
    │  │	 └─ _navigation_data
    │  │		├─ _navigation_items_.html
    │  │		├─ _search_and_language_.html
    │  │		└─ _special_offer_.html

###### Šablona pro domácí stránku

    │  ├─ 1_home
    │  │  ├─ 10__base__.html
    │  │  ├─ 11__hero__.html
    │  │  ├─ 12__intro__.html
    │  │  ├─ 13__featured_articles__.html
    │  │  ├─ 14__divider__.html
    │  │  ├─ 15__latest_articles__.html
    │  │  ├─ 16__newsletter__.html
    │  │  ├─ 17__gallery__.html
    │  │  ├─ _home_data
    │  │  │  ├─ __featured_articles__.html
    │  │  │  ├─ __latest_articles__.html
    │  │  │  ├─ _display_background_image_.html
    │  │  │  ├─ _display_div_text_.html
    │  │  │  ├─ _display_h1_text_.html
    │  │  │  ├─ _display_h2_text_.html
    │  │  │  ├─ _display_link_.html
    │  │  │  ├─ _edit_button_.html
    │  │  │  ├─ _gallery_articles_.html
    │  │  │  ├─ _input_email_field_.html
    │  │  │  ├─ _main_picture_.html
    │  │  │	 └─ _section_display_.html
    │  │  └─ _home_edit
    │  │	 ├─ __divider__.html
    │  │	 ├─ __featured__.html
    │  │	 ├─ __gallery__.html
    │  │	 ├─ __hero__.html
    │  │	 ├─ __intro__.html
    │  │	 ├─ __latest__.html
    │  │	 ├─ __newsletter__.html
    │  │	 └─ _edit_data
    │  │		├─ _edit_article_.html
    │  │		├─ _edit_background_image_.html
    │  │		├─ _edit_html_field_.html
    │  │		├─ _edit_link_.html
    │  │		└─ _submit_button_with_display_checkbox_.html

###### Šablona pro stránky zobrazující postranní panel

    │  ├─ 2_main
    │  │  ├─ 20__base__.html
    │  │  ├─ 21__sidebar__.html
    │  │  ├─ 22__search__.html
    │  │  ├─ 23__profile_update__.html
    │  │  ├─ _search_data
    │  │  │  ├─ _form_.html
    │  │  │	 └─ _form_data
    │  │  │		├─ _autor_input_.html
    │  │  │		├─ _collapse_button_.html
    │  │  │		├─ _date_inputs_.html
    │  │  │		├─ _error_messages_.html
    │  │  │		├─ _check_box_inputs_.html
    │  │  │		├─ _input_field_.html
    │  │  │		└─ _submit_button_md_.html
    │  │  └─ _sidebars
    │  │	 ├─ __category__.html
    │  │	 ├─ __search__.html
    │  │	 ├─ __tags__.html
    │  │	 ├─ __user__.html
    │  │	 └─ _data
    │  │		├─ _author_dropdown_menu_.html
    │  │		├─ _search_options_items_.html
    │  │		├─ _sidebar_movement_buttons_.html
    │  │		└─ _user_dropdown_items_.html

###### Šablona pro stránky zobrazující více článků

    │  ├─ 3_articles
    │  │  ├─ 30__base__.html
    │  │  ├─ 31__page_title__.html
    │  │  ├─ 32__page_navigation__.html
    │  │  ├─ 33__articles__.html
    │  │  ├─ 34__pagination__.html
    │  │  ├─ _articles_data
    │  │  │  ├─ _article_view_setup_.html
    │  │  │	 └─ _view_setup_data
    │  │  │		├─ _author_.html
    │  │  │		├─ _category_.html
    │  │  │		├─ _comment_count_.html
    │  │  │		├─ _main_picture_.html
    │  │  │		├─ _overview_.html
    │  │  │		├─ _published_ago_.html
    │  │  │		├─ _published_date_.html
    │  │  │		├─ _tags_.html
    │  │  │		└─ _title_.html
    │  │  └─ _page_navigation_data
    │  │	 ├─ _categories_.html
    │  │	 ├─ _my_articles_.html
    │  │	 ├─ _search_results_.html
    │  │	 ├─ _tags_.html
    │  │	 ├─ _search_result_data
    │  │	 │	├─ _tab_for_categories_.html
    │  │	 │	├─ _tab_for_results_and_similar_.html
    │  │	 │	├─ _tab_to_show_categories_.html
    │  │	 │	└─ _tab_to_show_results_and_similar_.html
    │  │	 └─ _tags_data
    │  │		├─ _tab_for_categories_.html
    │  │		├─ _tab_for_tag_and_similar_.html
    │  │		├─ _tab_to_show_categories_.html
    │  │		└─ _tab_to_show_tag_and_similar_.html

###### Šablona pro stránku zobrazující jeden článek

    │  ├─ 4_article
    │  │  ├─ 40__base__.html
    │  │  ├─ 41__article__.html
    │  │  ├─ 42__previous_and_next__.html
    │  │  ├─ 43__display_comments__.html
    │  │  ├─ 44__add_comment__.html
    │  │  ├─ _article_data
    │  │  │  ├─ _content_.html
    │  │  │  ├─ _main_picture_.html
    │  │  │  ├─ _next_.html
    │  │  │  ├─ _overview_.html
    │  │  │  ├─ _previous_.html
    │  │  │  ├─ _tags_.html
    │  │  │  ├─ _title_.html
    │  │  │	 └─ _update_article_.html
    │  │  └─ _comment_data
    │  │	 ├─ _add_comment_header_.html
    │  │	 ├─ _comment_author_picture_.html
    │  │	 ├─ _comment_creation_.html
    │  │	 ├─ _comment_display_.html
    │  │	 └─ _title_and_comment_count_.html

###### Šablona pro vytvoření a úpravu článku

    │  ├─ 5_create_article
    │  │  ├─ 50__base__.html
    │  │  ├─ 51__overview__.html
    │  │  ├─ 52__content__.html
    │  │  ├─ 53__settings__.html
    │  │  ├─ 54__confirm_leave__.html
    │  │  ├─ 55__confirm_delete__.html
    │  │  └─ _data
    │  │	 ├─ _buttons_both_.html
    │  │	 ├─ _input_category_.html
    │  │	 ├─ _input_next_article_.html
    │  │	 ├─ _input_previous_article_.html
    │  │	 ├─ _input_status_.html
    │  │	 ├─ _input_tags_.html
    │  │	 └─ _main_picture_view_.html

###### Přepsání vzhledu stránek AllAuth pro přihlášení a registraci

    │  ├─ account
    │  │  ├─ login.html
    │  │  ├─ signup.html
    │  │  ├─ _login
    │  │  │	 ├─ _email_input_.html
    │  │  │	 ├─ _help_links_.html
    │  │  │	 ├─ _login_with_google_.html
    │  │  │	 ├─ _or_separator_.html
    │  │  │	 ├─ _password_input_.html
    │  │  │	 ├─ _remember_me_.html
    │  │  │	 └─ _submit_button_.html
    │  │  ├─ _shared
    │  │  │  ├─ _base_.html
    │  │  │  ├─ _error_messages_.html
    │  │  │  ├─ _picture_.html
    │  │  │  ├─ _redirect_value_.html
    │  │  │	 └─ _script_for_showing_password_.html
    │  │  └─ _signup
    │  │	 ├─ _email_input_.html
    │  │	 ├─  _help_links_.html
    │  │	 ├─ _password_input1_.html
    │  │	 ├─ _password_input2_.html
    │  │	 ├─ _submit_button_.html
    │  └─ socialaccount	
    │	  └─ login.html

[<<< Přechod na stránku se stromovou strukturou celého projektu.](read_me_data/05_tree.md)