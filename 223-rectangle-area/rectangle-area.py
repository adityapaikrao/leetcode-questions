class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        rectangle 1
        xlims = [ax1, ax2] [-3 3]
        ylims = [ay1, ay2] [0, 4]
        area = 6 * 4 = 24

        rec 2 
        xlims [bx1, bx2] [0, 9]
        ylims [by1, by2] [-1, 2]
        area = 9 * 3 = 27

        x-overlap -> [-3, 3] [0, 9] => [0, 3]
        y-overlap -> [-1, 2] [0, 4]=> [0, 2]
        overlap area = 3 * 2 = 6

        [-1, 1] [0, 0]=> [0, 0]
        """
        xlims = [[ax1, ax2], [bx1, bx2]]
        xlims.sort()
        ylims = [[ay1, ay2], [by1, by2]]
        ylims.sort()

        # x & y overlaps
        x_overlap = y_overlap = 0
        if xlims[0][1] > xlims[1][0]:
            x_overlap = min(xlims[0][1], xlims[1][1]) - xlims[1][0]
        if ylims[0][1] > ylims[1][0]:
            y_overlap = min(ylims[0][1], ylims[1][1]) - ylims[1][0]
        
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlap_area = x_overlap * y_overlap

        return area1 + area2 - overlap_area
        
