# Calculator_Python
Приложение должно позволять пользователю ввести 4 числа. И выбрать одну из 4 операций(*+-/).
Обеспечить диапазон вводимых чисел и результата: не менее чем от минус 1 000 000 000 000.000000 до плюс 1 000 000 000 000.000000.  Если итоговый результат превышает указанный диапазон чисел, то допускается просто написать сообщение о переполнении. 
Для отделения дробной и целой части программа должна успешно принимать от пользователя как символ «точка», так и символ «запятая». Допускается автоматически менять ее на любой единый «удобный» вам разделитель (точку или запятую).
Калькулятор не должен выводить (или принимать на вход) числа в экспоненциальной нотации (например:123e+2)
При смене в операционной системе региональных настроек (разделителя чисел), программа должна по-прежнему корректно вычислять числа.
При делении округлять результат по правилам математики до 6 знаков после запятой.
Сообщать пользователю (выдавать ошибку) о невозможности деления на 0.
В результате вычислений отображать в результате расчетов только шесть знаков после запятой. Незначащие нули не отображать.
В результате вычислений разделителем целой и дробной части в результате всегда отображать «точку».
Разрешать пользователю вводить (с клавиатуры) числа с пробелами в качестве разделителей разрядов. При этом программа не должна принимать числа, когда разделителей пробелов много подряд или они не в нужных местах.  (например, программа должна считать ошибочными числа вида “1  23 5.67”).
Корректно (адекватно) обрабатывать ситуацию, когда пользователь ввел некорректно числа (например, ввел буквы). 
Считать некорректным ввод “0.0-1” в поле для одного числа
Обеспечить следующий приоритет (очередность) вычислений. Второй и третий операнд имеют приоритетный порядок вычислений (они всегда как бы «в скобах»). Очередность остальных операций – как принято в математике.
Все промежуточные вычисления всегда округлять до 10 знаков после запятой по правилам математического округления.
Если промежуточное вычисление выходит за диапазон 1 000 000 000 000.00000000000, то допускается писать переполнение и не считать.
После вывода результат добавить возможность выбора одного из трех видов округления итогового результата расчетов:
а) математическое;
б) бухгалтерское (банковское);
в) усечение.
Дополнительно после расчетов отображать округленное до целых чисел по выбранному методу значение.

