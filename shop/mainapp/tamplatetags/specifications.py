from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """
               <table class="table">
                <tbody>
             """

TABLE_TAIL = """
                 </tbody>
                </table>
             """

TABLE_CONTENT = """"
                  <tr>
                   <td>{name}</td>
                   <td>{value}</td>
                  </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge'
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'Разрешение экрана': 'resolution',
        'Заряд аккумулятора': 'accum_volume',
        'Оперативная память': 'ram',
        'Наличие слота для SD карты': 'sd',
        'Максимальный обьём SD карты': 'sd_volume_max',
        'Камера (МП)': 'main_cam_mp',
        'Фронтальная камера (МП)': 'frontal_cam_mp'
    },
    'smartwatch': {
        'Brand': 'brand',
        'Диагональ': 'diagonal',
        'Разрешение экрана': 'resolutions',
        'Датчики': 'sensors',
        'Видеокарта': 'video',
        'Совместимость с ОС': 'os',
        'Объём батарейи':'accum_volume',
        'Защита от воды и пыли':'protection = models'
    },
    'TV': {
        'Диагональ': 'diagonal',
        'Brand': 'brand',
        'Цвет': 'Color',
        'Разрешение экрана': 'resolutions',
        'Тип дисплея': 'display'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product, arg):
    print(arg, 'arg_value')
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
