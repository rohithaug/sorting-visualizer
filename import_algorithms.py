from algorithms.SelectionSort import SelectionSort
from algorithms.BubbleSort import BubbleSort
from algorithms.InsertionSort import InsertionSort
from algorithms.MergeSort import MergeSort
from algorithms.QuickSort import QuickSort
from algorithms.HeapSort import HeapSort
from algorithms.ShellSort import ShellSort
from algorithms.CombSort import CombSort
from algorithms.GnomeSort import GnomeSort
from algorithms.CocktailSort import CocktailSort
from algorithms.TimSort import TimSort
from algorithms.CycleSort import CycleSort
from algorithms.BitonicSort import BitonicSort
from algorithms.RadixSort import RadixSort
from algorithms.StoogeSort import StoogeSort
from algorithms.PancakeSort import PancakeSort

algorithms = {"Selection": SelectionSort(),
              "Bubble": BubbleSort(),
              "Insertion": InsertionSort(),
              "Merge": MergeSort(),
              "Quick": QuickSort(),
              "Heap": HeapSort(),
              "Shell": ShellSort(),
              "Comb": CombSort(),
              "Gnome": GnomeSort(),
              "Cocktail": CocktailSort(),
              "Tim": TimSort(),
              "Cycle": CycleSort(),
              "Bitonic": BitonicSort(),
              "Radix": RadixSort(),
              "Stooge": StoogeSort(),
              "Pancake": PancakeSort()}
