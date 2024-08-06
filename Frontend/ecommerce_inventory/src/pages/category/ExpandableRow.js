import { Box, Collapse, Typography, IconButton } from "@mui/material"
import { width } from "@mui/system"
import { DataGrid, GridRow, GridToolbar } from "@mui/x-data-grid"
import Add from '@mui/icons-material/Add'
import Delete from '@mui/icons-material/Delete'
import Edit from '@mui/icons-material/Edit'



const ExpandableRow = ({row, props, onAEditClick, onDeleteClick}) => {
    let columns = []
    if (row.children && row.children.length > 0) {
        columns = Object.keys(row.children[0]).map(key => ({
            field: key,
            headerName: key.charAt(0).toUpperCase() + key.slice(1).replaceAll('_', ' '),
            width: 150,
        })).filter((item) => {
            return item.field !== 'children'
        })

        columns = [{
            field: 'action', 
            headerName: 'Action',
            width: 180,
            sortable: false,
            renderCell: (params) => {
                return <>
                    <IconButton onClick={() => onAEditClick(params)}>
                        <Edit color='primary' />
                    </IconButton>

                    <IconButton onClick={() => onDeleteClick(params)}>
                        <Delete color='secondary' />
                    </IconButton>
                </>
            }
        }, ...columns]
    }

    return (
        <>
            <Box sx={{display: 'flex', alignItems: 'center'}}>
                <GridRow {...props} />
            </Box>
            <Collapse in={row?.open?row.open:false} timeout={"auto"} unmountOnExit>
                <Box margin={1}>
                    {
                        row.children && row.children.length > 0 ? 
                        <DataGrid 
                            rows={row.children}
                            columns={columns}
                            hideFooter
                            rowHeight={75}
                            autoHeight
                            rowSelection={false}
                            slots={{
                                toolbar: GridToolbar,
                            }}
                        /> :
                        <Typography variant="body2" align="center" textAlign="center" >No children Items</Typography>
                    }
                </Box>
            </Collapse>
        </>
    )
}

export default ExpandableRow