bool IsWeekend(short numDayOfWeek) =>
            numDayOfWeek == 6 ||
            numDayOfWeek == 7;

Console.Write("Введите номер дня недели: ");
var numDayOfWeek = short.Parse(Console.ReadLine());

if (IsWeekend(numDayOfWeek))
    Console.WriteLine($"{numDayOfWeek} -> да");
else
    Console.WriteLine($"{numDayOfWeek} -> нет");