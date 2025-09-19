const std = @import("std");

// Quick Sort function
fn quickSort(arr: []i32) void {
    if (arr.len <= 1) {
        return;
    }

    const pivot_index = partition(arr);

    // Split the array into left and right partitions
    // Note: Zig's slice splitting is slightly different from Rust's
    // We need to carefully handle the pivot element
    var left_slice = arr[0..pivot_index];
    var right_slice = arr[pivot_index + 1 .. arr.len]; // Exclude the pivot from the right slice

    quickSort(left_slice);
    quickSort(right_slice);
}

// Partition function
fn partition(arr: []i32) usize {
    const len = arr.len;
    // For simplicity, we'll use the last element as the pivot, similar to the Rust example.
    // In a production quicksort, you might choose a random pivot or median-of-three for better average case performance.
    const pivot = arr[len - 1];
    var i: usize = 0; // Index of the smaller element

    for (0..(len - 1)) |j| {
        if (arr[j] <= pivot) {
            std.mem.swap(i32, &arr[i], &arr[j]);
            i += 1;
        }
    }

    // Place the pivot at its correct position
    std.mem.swap(i32, &arr[i], &arr[len - 1]);

    return i;
}

pub fn main() !void {
    var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };

    // Create a mutable slice from the array for the quicksort function
    var slice: []i32 = &arr;

    std.debug.print("Before: {any}\n", .{slice});

    quickSort(slice);

    std.debug.print("After: {any}\n", .{slice});
}
