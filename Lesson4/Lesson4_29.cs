using System.Text;
IReadOnlyCollection<int> GenerateRandomIntArray(int n = 8)
{
    var array = new List<int>();
    var rnd = new Random();

    while (n > 0)
    {
        int itemNew = rnd.Next();
        array.Add(itemNew);
        n--;
    }

    return array;
}
void PrintIntArray(in IReadOnlyCollection<int> array)
{
    var arrOutput = new StringBuilder();

    foreach (var item in array)
    {
        arrOutput.Append(item)
                 .Append(" ");
    }
    Console.WriteLine(arrOutput.ToString()
                               .Trim());
}

var arrayRandom = GenerateRandomIntArray();
Console.Write("Сгенерированный массив случайных чисел: ");
PrintIntArray(arrayRandom);