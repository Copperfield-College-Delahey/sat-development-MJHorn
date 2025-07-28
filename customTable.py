import customtkinter as ctk

class CustomTableWithSelection:
    def __init__(self, master, data, column_widths=None, selection_callback=None, 
                 header_color=None, row_colors=None, selected_color=None, hover_color=None,
                 header_text_color=None, row_text_color=None, selected_text_color=None):
        self.master = master
        self.data = data
        self.column_widths = column_widths or [100] * len(data[0])
        self.selection_callback = selection_callback
        self.selected_row = None
        
        # Color configuration - normalize single colors to tuples
        self.header_color = self._normalize_color(header_color) or ("gray75", "gray25")
        self.row_colors = self._normalize_color(row_colors) or ("gray90", "gray13")
        self.selected_color = self._normalize_color(selected_color) or ("lightblue", "darkblue")
        self.hover_color = self._normalize_color(hover_color) or ("gray85", "gray20")
        
        # Text color configuration
        self.header_text_color = self._normalize_color(header_text_color) or ("black", "white")
        self.row_text_color = self._normalize_color(row_text_color) or ("black", "white")
        self.selected_text_color = self._normalize_color(selected_text_color) or ("black", "white")
        
        # Create main frame
        self.frame = ctk.CTkFrame(master)
        
        # Configure grid columns with exact fixed widths
        for col_idx, width in enumerate(self.column_widths):
            self.frame.grid_columnconfigure(col_idx, weight=0, minsize=width)
        
        # Create cells
        self.cells = []
        self.create_table()
    
    def _normalize_color(self, color):
        """Convert single color to tuple format if needed"""
        if color is None:
            return None
        if isinstance(color, str):
            return (color, color)  # Use same color for light and dark mode
        return color
    
    def truncate_text(self, text, max_length):
        """Truncate text with ellipsis if it exceeds max_length"""
        text_str = str(text)
        if len(text_str) > max_length:
            return text_str[:max_length-3] + "..."
        return text_str
    
    def create_table(self):
        # Properly destroy all widgets in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()
            
        self.cells = []

        # Character limits for each column [Question Text, Tags, Source] - Question ID is hidden
        char_limits = [50, 40, 20]

        for row_idx, row_data in enumerate(self.data):
            row_cells = []
            for col_idx, cell_data in enumerate(row_data):
                # Determine colors based on header row or selection
                is_header = row_idx == 0
                
                if is_header:
                    base_color = self.header_color
                    cell_hover_color = self.header_color  # Header doesn't change on hover
                    text_color = self.header_text_color
                    display_text = str(cell_data)  # Don't truncate headers
                else:
                    base_color = self.row_colors
                    cell_hover_color = self.hover_color
                    text_color = self.row_text_color
                    # Apply character limit with truncation
                    char_limit = char_limits[col_idx] if col_idx < len(char_limits) else 20
                    display_text = self.truncate_text(cell_data, char_limit)
                
                # Get column width, ensuring we don't exceed array bounds
                cell_width = self.column_widths[col_idx] if col_idx < len(self.column_widths) else 100
                
                # Create clickable cell - place directly in main frame
                cell = ctk.CTkButton(
                    self.frame,
                    text=display_text,
                    width=cell_width,
                    height=30,
                    corner_radius=5,
                    fg_color=base_color,
                    hover_color=cell_hover_color,
                    text_color=text_color,
                    command=lambda r=row_idx: self.select_row(r) if r > 0 else None,  # Don't select header
                    cursor="hand2" if not is_header else "arrow",
                    anchor="w"  # Left-align text for better appearance
                )
                
                # Grid the cell and force it to NOT expand
                cell.grid(row=row_idx, column=col_idx, padx=1, pady=1, sticky="")
                
                # Force the button to maintain its exact width
                cell.configure(width=cell_width)
                cell.bind("<Configure>", lambda e, w=cell_width, c=cell: c.configure(width=w))
                
                row_cells.append(cell)
            
            self.cells.append(row_cells)
    
    def select_row(self, row_idx):
        """Select a row and update colors"""
        if row_idx == 0:  # Don't select header
            return
            
        # Deselect previous row
        if self.selected_row is not None:
            self.update_row_colors(self.selected_row, selected=False)
        
        # Select new row
        self.selected_row = row_idx
        self.update_row_colors(row_idx, selected=True)
        
        # Call callback if provided
        if self.selection_callback:
            self.selection_callback(row_idx, self.data[row_idx])
    
    def update_row_colors(self, row_idx, selected=False):
        """Update colors for a specific row"""
        if row_idx == 0:  # Header row
            return
            
        if selected:
            color = self.selected_color
            hover_color = self.selected_color  # Keep same color on hover when selected
            text_color = self.selected_text_color
        else:
            color = self.row_colors
            hover_color = self.hover_color
            text_color = self.row_text_color
        
        for cell in self.cells[row_idx]:
            cell.configure(fg_color=color, hover_color=hover_color, text_color=text_color)
    
    def get_selected_row(self):
        """Get the currently selected row data"""
        if self.selected_row is not None:
            return self.selected_row, self.data[self.selected_row]
        return None, None
    
    def deselect_row(self):
        """Deselect the current row"""
        if self.selected_row is not None:
            self.update_row_colors(self.selected_row, selected=False)
            self.selected_row = None
    
    def set_column_widths(self, widths):
        """Update column widths"""
        self.column_widths = widths
        
        # Update main frame grid configuration
        for col_idx, width in enumerate(widths):
            self.frame.grid_columnconfigure(col_idx, weight=0, minsize=width)
        
        # Update existing cells
        for row_idx, row_cells in enumerate(self.cells):
            for col_idx, cell in enumerate(row_cells):
                if col_idx < len(widths):
                    cell.configure(width=widths[col_idx])

    def update_data(self, new_data):
        """Update table with new data"""
        self.data = new_data
        self.selected_row = None
                
        # Recreate table
        self.create_table()
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        self.frame.grid(**kwargs)