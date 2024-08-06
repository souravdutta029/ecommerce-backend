import { Alert, Box, FormControl, FormControlLabel, InputLabel, MenuItem, Select, Switch, TextField } from '@mui/material';
import { useFormContext } from 'react-hook-form';

const StepFileComponents = ({formConfig, fieldType}) => {
    const {register, formState: {errors}} = useFormContext();
    const fileFields = formConfig.data.file
    return (
        <Box>
            {fileFields.map((field, index) => (
                <>
                    <Box component={"div"} className='fileInput'>
                        <label>{field.label}</label>
                        <input type="file" {...register(field.name, {required:field.required})} />
                    </Box>
                    {
                        !!errors[field.name] && <Alert severity="error" variant='outlined' sx={{mt:2}}>
                            This field is required
                        </Alert>
                    }
                </>
            ))}
        </Box>
    )
}

export default StepFileComponents