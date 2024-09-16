
def fill_input_text(input_field, value):
    input_field.clear()  # Limpia el campo si ya tiene contenido
    input_field.send_keys(value)




# dropdown = Select(driver.find_element(By.ID, "mi_dropdown"))
# dropdown.select_by_value("opcion1")  # O select_by_visible_text("Opción 1")