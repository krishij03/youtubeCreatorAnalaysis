export const userColumns = [
  { field: "id", headerName: "ID", width: 70 },
  {
    field: "thumbnail",
    headerName: "Thumbnail",
    width: 100,
    height: 50,
    renderCell: (params) => {
      return (
        <div className="cellWithImg">
          <img className="cellImg" src={params.row.img} alt="avatar" />
          {params.row.username}
        </div>
      );
    },
  },
  {
    field: "title",
    headerName: "Title",
    width: 500,
  },
  {
    field: "sentimentalScore",
    headerName: "Sentimental Score",
    width: 150,
  },
];

//temporary data
export const userRows = [
  {
    id: 1,
    img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
    title: "Spending a night at the world's scariest hotel" ,
    sentimentalScore: "97%",
  },
  {
    id: 2,
    img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
    title: "Title for row 2",
    sentimentalScore: "80%",
  },
  {
    id: 3,
    img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
    title: "Title for row 3",
    sentimentalScore: "75%",
  },
  {
    id: 4,
    img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
    title: "Title for row 4",
    sentimentalScore: "90%",
  },
  {
    id: 5,
    img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
    title: "Title for row 5",
    sentimentalScore: "85%",
  },
  {
    id: 6,
    img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
    title: "Title for row 6",
    sentimentalScore: "95%",
  },
];
