## Практическое задание по routing
В этом задании нужно будет построить навигацию веб-приложения, написать view, которые умеют получать и оперировать различными параметрами из запроса (параметры из URL, GET параметры, POST параметры), и сформировать простые HTTP ответы с различными статусами.

1. Нужно написать view simple_route, которая формирует http ответ с пустым телом со статусом 200 на запрос GET (если запросы отличные от GET - возвращать 405) по /routing/simple_route/
2. slug_route - нужно написать view, которая принимает slug и отдает его в теле ответа. В slug допустимы символы: 0-9, a-z, -, _ . Минимальная длина 1 символ, максимальная длина 16.
3. sum_route - нужно написать view, которая принимает 2 числа и их суммирует, например /routing/sum_route/1/2/
4. sum_get_method - нужно написать view, которая принимает 2 числа из GET параметров a и b и суммирует их. Допускается только метод GET. Например /routing/sum_get_method/?а=1&b=2
5. sum_post_method - нужно написать view, которая принимает 2 числа из POST параметров a и b и суммирует их. Допускается только метод POST. Например /routing/sum_post_method/

Ссылки:
* [urls](https://github.com/Daniil-Solo/Programming-in-Python-Specialization/blob/main/Web_services/routing/core/urls.py)
* [views](https://github.com/Daniil-Solo/Programming-in-Python-Specialization/blob/main/Web_services/routing/core/views.py)
