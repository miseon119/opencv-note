void contourOffset(const std::vector<cv::Point>& src, std::vector<cv::Point>& dst, const cv::Point& offset) {
    dst.clear();
    dst.resize(src.size());
    for (int j = 0; j < src.size(); j++)
        dst[j] = src[j] + offset;

}
void scaleContour(const std::vector<cv::Point>& src, std::vector<cv::Point>& dst, float scale)
{
    cv::Rect rct = cv::boundingRect(src);

    std::vector<cv::Point> dc_contour;
    cv::Point rct_offset(-rct.tl().x, -rct.tl().y);
    contourOffset(src, dc_contour, rct_offset);

    std::vector<cv::Point> dc_contour_scale(dc_contour.size());

    for (int i = 0; i < dc_contour.size(); i++)
        dc_contour_scale[i] = dc_contour[i] * scale;

    cv::Rect rct_scale = cv::boundingRect(dc_contour_scale);

    cv::Point offset((rct.width - rct_scale.width) / 2, (rct.height - rct_scale.height) / 2);
    offset -= rct_offset;
    dst.clear();
    dst.resize(dc_contour_scale.size());
    for (int i = 0; i < dc_contour_scale.size(); i++)
        dst[i] = dc_contour_scale[i] + offset;
    }

void scaleContours(const std::vector<std::vector<cv::Point>>& src, std::vector<std::vector<cv::Point>>& dst, float scale)
{
    dst.clear();
    dst.resize(src.size());
    for (int i = 0; i < src.size(); i++)
        scaleContour(src[i], dst[i], scale);
}
        void main(){
            std::vector<std::vector<cv::Point>> src,dst;
            scaleContours(src,dst,0.95);
         }
