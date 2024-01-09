using System;
using System.IO;

namespace inputProcessCS
{
    class Program
    {
        static void Main()
        {
            // path for the inputs from the question
            string filePath = "../inputs.txt";

            try
            {            
                string[] lines = File.ReadAllLines(filePath);
                int i = 0;
                int sum = 0;
                foreach (string line in lines)
                {
                    i++;
                    int value = processLine(line);
                    Console.WriteLine($"Line number {i} is: {line} \nvalue:{value}");
                    sum+=value;
                }
                Console.WriteLine($"the sum is {sum}");
            }
            catch (IOException e)
            {
                Console.WriteLine($"An error occurred while reading the file: {e.Message}");
            }
        }

        // Gets a Line as an input and retuns the value as described in the quest
        public static int processLine(string line)
        {
            int firstDig = 0;
                for (int i = 0; i < line.Length; i++)            
                    if (char.IsDigit(line[i]))
                    {
                        firstDig = int.Parse(line[i].ToString());
                        break;
                    }
                int lastDig = firstDig;
                for (int i = line.Length -1; i >= 0; i--)
                    if (char.IsDigit(line[i]))
                    {
                        lastDig = int.Parse(line[i].ToString());
                        break;
                    }
                return (firstDig * 10) + lastDig;
        }
        
    }   
}
