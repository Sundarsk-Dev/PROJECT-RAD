# File: FileCleaner.py

import random

class FileCleaner:
    """
    RAD Project: The File De-duplicator Utility
    
    Implements the Two Pointers technique to efficiently and in-place 
    move 'redundant' files (represented by size 0) to the end of a list.
    """

    def __init__(self, file_sizes: list[int]):
        """Initializes the utility with a list of file sizes."""
        # Work on a copy of the input for demonstration
        self.file_sizes = list(file_sizes)
        self.original_state = list(file_sizes) 
        
    def clean_directory(self) -> None:
        """
        Core DSA Implementation: Moves all 0s to the end using the Two Pointers method.
        Time Complexity: O(N) | Space Complexity: O(1) (In-place operation)
        """
        
        # The 'write_ptr' marks where the next non-zero element should be placed.
        write_ptr = 0
        N = len(self.file_sizes)
        
        # The 'read_ptr' scans the entire array.
        for read_ptr in range(N):
            
            # If a non-zero element is found (a 'good' file)...
            if self.file_sizes[read_ptr] != 0:
                
                # We use the SWAP method for the clearest demonstration of Two Pointers.
                # Swap the non-zero element with the element at the 'write_ptr' position.
                # If read_ptr == write_ptr, the element is already correct, so we skip the swap.
                if read_ptr != write_ptr:
                    self.file_sizes[read_ptr], self.file_sizes[write_ptr] = \
                        self.file_sizes[write_ptr], self.file_sizes[read_ptr]
                
                # Advance the write pointer to reserve the next spot for a non-zero element.
                write_ptr += 1

    def get_summary(self):
        """Calculates a summary for the display."""
        zero_count = self.file_sizes.count(0)
        non_zero_count = len(self.file_sizes) - zero_count
        return {
            "Original": self.original_state,
            "Cleaned": self.file_sizes,
            "Non_Zero_Files": self.file_sizes[:non_zero_count],
            "Corrupt_Count": zero_count
        }

    def display_ui(self):
        """Prints the pitch and the results with a simple UI."""
        summary = self.get_summary()
        
        # --- The Project Pitch (The "Efficient Point") ---
        print("\n" + "=" * 70)
        print("💡 RAD Project: The File De-duplicator Utility - In-Place Cleanup")
        print("=" * 70)
        
        print("🎯 **PITCH:** When cleaning file systems, we need speed and low memory usage.")
        print("   This utility demonstrates an **O(N) single-pass** algorithm to segment")
        print("   'good' files (non-zero size) from 'corrupt' files (size 0) **without**")
        print("   creating a new list, dominating slow, memory-intensive methods.")
        print("   It leverages the **Two Pointers** pattern for **in-place O(1) space** efficiency.")
        
        print("\n" + "-" * 70)
        print("📁 Directory State BEFORE Cleanup (Simulated Files):")
        print(f"   {summary['Original']}")
        
        # --- Run the Core DSA Algorithm ---
        self.clean_directory()
        
        # --- Results Display ---
        print("\n" + "-" * 70)
        print("✨ Directory State AFTER Cleanup (Two Pointers Applied):")
        print(f"   Cleaned List: {summary['Cleaned']}")
        print(f"\n   ✅ **Good Files (Order Preserved):** {summary['Non_Zero_Files']}")
        print(f"   🗑️ **Corrupt/Redundant Count:** {summary['Corrupt_Count']}")
        print("-" * 70)


# --- Driver Code (Simulating Real-World Scenarios) ---

# Sample 1: Standard Use Case
sample_files_1 = [0, 25, 100, 0, 45, 8, 0, 120, 50]
cleaner_1 = FileCleaner(sample_files_1)
cleaner_1.display_ui()

# Sample 2: Heavy Redundancy Case
sample_files_2 = [0, 0, 800, 0, 0, 15, 0, 0, 0, 20]
cleaner_2 = FileCleaner(sample_files_2)
cleaner_2.display_ui()

# Sample 3: A large, Random Scenario
random_list = [random.choice([0, 10, 50, 120, 200, 0, 0, 80]) for _ in range(15)]
cleaner_3 = FileCleaner(random_list)
cleaner_3.display_ui()